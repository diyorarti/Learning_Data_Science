"""
create a procedure order_risk_summary:
    The procedure should analyze one order and classify it according to its payment amount and review score

    Parameters:
        p_order_id VARCHAR(50)
    
    Variables:
        v_total_payment NUMERIC(12, 2); -> total payment for the order
        v_review_score  NUMERIC; -> review score of the order
        v_order_status TEXT; -> Current order status
        v_risk_level TEXT; -> classification by condition

    Classifying the order:
        order_status != 'delivered' -> incomplete order
        total_payment >= 500 AND review score <= 2 -> high risk order
        total_payment >= 200 AND review score <= 3 -> medium risk order
        review score >= 4 -> Low risk
        none of them -> Normal
""";

CREATE OR REPLACE PROCEDURE order_risk_summary(
    p_order_id VARCHAR(50)
) 
LANGUAGE plpgsql
AS
$$

DECLARE
    v_total_payment NUMERIC(12, 2);
    v_review_score NUMERIC;
    v_order_status TEXT;
    v_risk_level TEXT;

BEGIN 
    SELECT 
        SUM(p.payment_value),
        AVG(r.review_score),
        o.order_status

    INTO 
        v_total_payment,
        v_review_score,
        v_order_status

    FROM orders o
    JOIN order_payments p ON o.order_id = p.order_id
    JOIN order_reviews r ON o.order_id = r.order_id
    WHERE o.order_id = p_order_id;

    IF v_order_status != 'delivered' THEN v_risk_level:='incomplete order'
    ELSIF v_total_payment >= 500 AND v_review_score <= 2 THEN v_risk_level:='high risk order'
    ELSIF v_total_payment >= 200 AND v_review_score <= 3 THEN v_risk_level:='medium risk order'
    ELSIF v_review_score >= 4 THEN v_risk_level:='low risk order'
    ELSE v_risk_level:='Normal order'
    END IF;

    RAISE NOTICE 'Total payment: %', v_total_payment;
    RAISE NOTICE 'Avergae review score: %', v_review_score;
    RAISE NOTICE 'Order status: %', v_order_status;
    RAISE NOTICE 'Order risk level: %', v_risk_level;

END;
$$;



