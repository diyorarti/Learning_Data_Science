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

    
"""