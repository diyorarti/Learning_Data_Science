"""
create a stored procedure process_customer_orders
    the procedure should analyze all orders of one customer during a specified period, classify each order and 
    save the results into a seperate reporting table

        First create this practice table
            customer_order_report(
            report_id BIGSERIAL PRIMARY KEY,
            customer_id VARCHAR(50),
            order_id VARCHAR(50),
            order_status TEXT,
            payment_amount NUMERIC(12,2),
            review_score NUMERIC(4,2),
            classification TEXT,
            requires_attention BOOLEAN DEFAULT FALSE,
            processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        The procedure will manipulate this table

        Parameters(the procedure should receive)
            p_customer_id VARCHAR(50)
            p_start_date TIMESTAMP
            p_end_date TIMESTAMP

        Variables
            v_order RECORD;
            v_payment NUMERIC(12, 2);
            v_review_score NUMERIC(4, 2);
            v_classification TEXT;

            v_total_orders BIGINT :=0;
            v_total_spent NUMERIC(12, 2) :=0;
            v_high_value_orders BIGINT :=0;
            v_problem_orders BIGINT :=0;

        Part-1 DELETE
            before generating a new report for the customer, remove their previous report rows
                CALL procedure first time
                        ↓
                report generated

                CALL again
                        ↓
                old report removed
                        ↓
                fresh report generated

        Part-2 FOR loop + SELECT 
            loop through the customer's orders from the specified period.

        Part-3 Caculate payment
            for each order calculate SUM(payment_value) from order_payments 
            and store it in v_payment

        Part-4 Calculate review score
            for every order calculate AVG(review_score) from order_review
            and store it in v_review_score

        Part-5 Conditional classification
            classify every order using the following rules:
                IF status = 'canceled'
                    → 'Canceled Order'

                ELSIF status != 'delivered'
                    → 'Incomplete Order'

                ELSIF payment >= 300
                    AND review_score <= 2
                    → 'High Value / Poor Review'

                ELSIF payment >= 300
                    → 'High Value Order'

                ELSIF review_score <= 2
                    → 'Poor Review Order'

                ELSE
                    → 'Normal Order'
        Part-6 INSERT 
            after classifying the current order, insert it into: customer_order_report

        PART-7 UPDATE
            after inserting a row, makrt it as requiring attention when the classification is one of:
                Canceled Order
                Incomplete Order
                High Value / Poor Review
                Poor Review Order

        Part-8 UPDATING counters
            Every order → v_total_orders + 1
            Every payment → add to v_total_spent
            Payment >= 300 → v_high_value_orders + 1
            Canceled / incomplete / poor-review order → v_problem_orders + 1

        Part-9 Print every processed order
            inside the loop, print:
                Order ID 
                Status
                Payment
                Review score 
                Classification

        PART-10 After END LOOP, print
            Customer ID
            Total orders processed
            Total spent
            High-value orders
            Problem orders
"""

-- Creating practice table
CREATE TABLE customer_order_report (
    report_id BIGSERIAL PRIMARY KEY,
    customer_id VARCHAR(50),
    order_id VARCHAR(50),
    order_status TEXT,
    payment_amount NUMERIC(12,2),
    review_score NUMERIC(4, 2),
    classification TEXT,
    requires_attention BOOLEAN DEFAULT FALSE,
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE PROCEDURE process_customer_orders(
    p_customer_id VARCHAR(50),
    p_start_date TIMESTAMP,
    p_end_date TIMESTAMP
)
LANGUAGE plpgsql
AS $$
DECLARE 
    v_order RECORD;
    v_payment NUMERIC(12, 2);
    v_review_score NUMERIC(4, 2);
    v_classification TEXT;

    v_total_orders BIGINT:=0;
    v_total_spent NUMERIC(12, 2):=0;
    v_high_value_orders BIGINT:=0;
    v_problem_orders BIGINT:=0;

BEGIN 
    -- DELETE previous report rows
    DELETE FROM customer_order_report
    WHERE customer_id = p_customer_id;

    -- loop customer's orders for the specified period
    FOR v_order IN 
        SELECT
            order_id,
            order_status,
            order_purchase_timestamp
        FROM orders
        WHERE customer_id = p_customer_id AND 
        order_purchase_timestamp BETWEEN p_start_date AND p_end_date

    LOOP
        -- calculating payment 
        SELECT SUM(payment_value)
        INTO v_payment
        FROM order_payments 
        WHERE order_id = v_order.order_id;

        -- if there is no payment
        IF v_payment = NULL THEN 
            v_payment := 0; 
        END IF;

        -- calculating v_review_score
        SELECT AVG(review_score)
        INTO v_review_score
        FROM order_reviews
        WHERE order_id = v_order.order_id;

        -- Conditional classification
        if v_order.order_status = 'canceled' THEN 
            v_classification:='Canceled Order';
        ELSIF v_order.order_status != 'delivered' THEN
            v_classification:='incomplete Order';
        ELSIF v_payment >= 300 AND v_review_score <= 2 THEN 
            v_classification:='High value / poor review Order';
        ELSIF v_payment >= 300 THEN
            v_classification:='High value Order';
        ELSIF v_review_score <= 2 THEN 
            v_classification:='Poor Review Order';
        ELSE
            v_classification:='Normal Order';
        END IF;

        --  INSERT 
        INSERT INTO customer_order_report(
            customer_id,
            order_id,
            order_status,
            payment_amount,
            review_score,
            classification
        )
        VALUES(
            p_customer_id,
            v_order.order_id,
            v_order.order_status,
            v_payment,
            v_review_score,
            v_classification
        );

        -- UPDATE
        IF v_classification IN ('Canceled Order', 
                                'incomplete Order', 
                                'High value / poor review Order',
                                'Poor Review Order'
                            ) THEN 
            UPDATE customer_order_report
            SET requires_attention = TRUE
            WHERE customer_id = p_customer_id AND order_id = v_order.order_id;
        END IF;

        -- Counters
        v_total_orders:= v_total_orders + 1;
        v_total_spent:= v_total_spent + v_payment;
        IF v_payment >= 300 THEN 
            v_high_value_orders:= v_high_value_orders + 1;
        END IF;
        IF v_classification IN ('Canceled Order', 
                                'incomplete Order', 
                                'High value / poor review Order',
                                'Poor Review Order'
                            ) THEN
            v_problem_orders:= v_problem_orders + 1;
        END IF;

        RAISE NOTICE 'ORDER ID: %', v_order.order_id;
        RAISE NOTICE 'Status: %', v_order.order_status;
        RAISE NOTICE 'Payment: %', v_payment;
        RAISE NOTICE 'Review: %', v_review_score;
        RAISE NOTICE 'Classification: %', v_classification;

        END LOOP;

    RAISE NOTICE 'Customer ID: %', p_customer_id;
    RAISE NOTICE 'Total Orders: %', v_total_orders;
    RAISE NOTICE 'Total Spent: %', v_total_spent;
    RAISE NOTICE 'High-value Orders : %', v_high_value_orders;
    RAISE NOTICE 'Problem Orders: %', v_problem_orders;
END;
$$;
        

SELECT 
    order_id,
    customer_id
FROM orders




CALL process_customer_orders(
    '494dded5b201313c64ed7f100595b95c',
    '2017-01-01',
    '2018-01-01'
);

SELECT * 
FROM customer_order_report


