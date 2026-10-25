"""
create a stored procedure: customer_order_activity_report()
    this procedure should analyze all orders of one customer within a specified period, 
    process them one by one using a loop, and finally classify the customer. 

Parameters:
    p_customer_id VARCHAR(50)
    p_start_date TIMESTAMP
    p_end_date TIMESTAMP

Variables:
    v_total_orders BIGINT :=0;
    v_delivered_orders BIGINT :=0;
    v_cancelled_orders BIGINT :=0;
    v_high_value_orders BIGINT :=0;
    v_total_spent NUMERIC(12, 2) :=0;
    v_customer_level TEXT;

    v_order_payment NUMERIC(12, 2);
    v_review_score NUMERIC; 
    v_order RECORD;

Loop through the customer's orders
    the loop should process orders where:
        customer_id = p_customer_id
        purchase timestamp >= p_start_date
        purchase timestamp < p_end_date

    For each order, v_order should contain at least:
        order_id
        order_status
        order_purchase_timestamp

    Count every order inside loop:

    Calculate payment for the current order

    Get the review score

    Classify each order
        IF order status = 'canceled'
            → print 'Canceled Order'
            → increase v_cancelled_orders

        ELSIF order status != 'delivered'
            → print 'Incomplete Order'

        ELSIF order payment >= 300
            → print 'High Value Delivered Order'
            → increase v_delivered_orders
            → increase v_high_value_orders

        ELSE
            → print 'Normal Delivered Order'
            → increase v_delivered_orders
    
    Print every order inside the loop

    Classify the customer after the loop

"""

CREATE OR REPLACE PROCEDURE customer_order_activity_report(
    p_customer_id VARCHAR(50),
    p_start_date TIMESTAMP,
    p_end_date TIMESTAMP
)
LANGUAGE plpgsql
AS $$
DECLARE 
    v_total_orders BIGINT := 0;
    v_cancelled_orders BIGINT := 0;
    v_delivered_order BIGINT := 0;
    v_high_value_orders BIGINT := 0;
    v_total_spent NUMERIC(12, 2) := 0;

    v_order_classification TEXT;
    v_customer_level TEXT;

    v_order_payment NUMERIC(12, 2);
    v_review_score NUMERIC; 
    v_order RECORD;

BEGIN 

    FOR v_order IN 
        SELECT
            order_id,
            order_status,
            order_purchase_timestamp
        FROM orders
        WHERE customer_id = p_customer_id
          AND order_purchase_timestamp >= p_start_date
          AND order_purchase_timestamp < p_end_date
    LOOP

        v_total_orders := v_total_orders + 1; 


        SELECT SUM(payment_value)
        INTO v_order_payment
        FROM order_payments 
        WHERE order_id = v_order.order_id;


        IF v_order_payment IS NULL THEN 
            v_order_payment := 0;
        END IF;


        SELECT AVG(review_score)
        INTO v_review_score
        FROM order_reviews
        WHERE order_id = v_order.order_id;


        IF v_order.order_status = 'canceled' THEN 

            v_order_classification := 'Cancelled order';
            v_cancelled_orders := v_cancelled_orders + 1;

        ELSIF v_order.order_status != 'delivered' THEN 

            v_order_classification := 'Incomplete order';

        ELSIF v_order_payment >= 300 THEN 

            v_order_classification := 'High value delivered order';
            v_delivered_order := v_delivered_order + 1;
            v_high_value_orders := v_high_value_orders + 1;
            v_total_spent := v_total_spent + v_order_payment;

        ELSE 

            v_order_classification := 'Normal delivered order';
            v_delivered_order := v_delivered_order + 1;
            v_total_spent := v_total_spent + v_order_payment;

        END IF;


        RAISE NOTICE 'Order ID: %', v_order.order_id;
        RAISE NOTICE 'Status: %', v_order.order_status;
        RAISE NOTICE 'Payment: %', v_order_payment;
        RAISE NOTICE 'Review: %', v_review_score;
        RAISE NOTICE 'Classification: %', v_order_classification;

    END LOOP;


    IF v_total_orders = 0 THEN 

        v_customer_level := 'No activity';

    ELSIF v_total_spent >= 2000
          AND v_delivered_order >= 5 THEN 

        v_customer_level := 'VIP Customer';

    ELSIF v_total_spent >= 500
          OR v_delivered_order >= 3 THEN 

        v_customer_level := 'Regular Customer';

    ELSE

        v_customer_level := 'Low Activity Customer';

    END IF;


    RAISE NOTICE 'Customer ID: %', p_customer_id;
    RAISE NOTICE 'Total orders: %', v_total_orders;
    RAISE NOTICE 'Delivered orders: %', v_delivered_order;
    RAISE NOTICE 'Canceled orders: %', v_cancelled_orders;
    RAISE NOTICE 'High-value orders: %', v_high_value_orders;
    RAISE NOTICE 'Total spent: %', v_total_spent;
    RAISE NOTICE 'Customer level: %', v_customer_level;

END;
$$;

CALL customer_order_activity_report(
    '9bdf08b4b3b52b5526ff42d37d47f222',
    '2018-01-01',
    '2019-01-01'
)

SELECT *
FROM orders
