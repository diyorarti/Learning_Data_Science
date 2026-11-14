-- Product Order Batch Processor
"""
Create a stored procedure called: process_order_batch:
    it's jobs is to process all pending product orders belong to one batch
    The key transaction rule:
        if a critical problem occurs while processing the batch, all changes already made for that batch must be undone
        with "ROLLBACK". If the whole batch finishes successfully, use "COMMIT"

1-step: Practice tables:
    products_invetory table:
    "CREATE TABLE products_inventory (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        stock_quantity INTEGER,
        price NUMERIC(10,2)
    );"

    order_requests table:
    "CREATE TABLE order_requests (
        request_id BIGSERIAL PRIMARY KEY,
        batch_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        status TEXT DEFAULT 'pending'
    );"

    reporting table:
    "CREATE TABLE order_processing_report (
        report_id BIGSERIAL PRIMARY KEY,
        batch_id INTEGER,
        request_id BIGINT,
        product_id INTEGER,
        quantity INTEGER,
        total_value NUMERIC(12,2),
        result TEXT,
        processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );"

    value:
    "INSERT INTO products_inventory
    VALUES
        (1, 'Laptop', 10, 2500.00),
        (2, 'Mouse', 50, 80.00),
        (3, 'Keyboard', 20, 150.00);"

2-step: Parameters:
    the procedure should receive:
        p_batch_id:         unique id for batch
        p_chunk_size:       how many units of stock may be reduced during one WHILE iteration

3-step: Variables:
    current request
    current product

    product stock
    product price

    requested quantity
    remaining quantity
    current chunk

    total order value

    batch failed?
    failure reason

4-step: DELETE:
    before processing the batch, delete the previous report for that batch
    
5-step: LOOP:
    use basic LOOP ... END LOOP;
    
""";