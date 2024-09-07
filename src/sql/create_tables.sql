-- SQL script to create all necessary tables
CREATE TABLE IF NOT EXISTS metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT NOT NULL,
    field_name TEXT NOT NULL,
    data_type TEXT NOT NULL,
    is_nullable BOOLEAN NOT NULL,
    is_primary_key BOOLEAN NOT NULL,
    is_testable BOOLEAN NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS test_definitions (
    test_id INTEGER PRIMARY KEY AUTOINCREMENT,
    test_name TEXT NOT NULL,
    test_description TEXT,
    test_type TEXT NOT NULL,
    function_name TEXT NOT NULL,
    parameters TEXT
);

CREATE TABLE IF NOT EXISTS test_configuration (
    config_id INTEGER PRIMARY KEY AUTOINCREMENT,
    metadata_id INTEGER,
    test_id INTEGER,
    FOREIGN KEY (metadata_id) REFERENCES metadata(id),
    FOREIGN KEY (test_id) REFERENCES test_definitions(test_id)
);

CREATE TABLE IF NOT EXISTS test_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    config_id INTEGER,
    test_passed BOOLEAN,
    test_output TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (config_id) REFERENCES test_configuration(config_id)
);

CREATE TABLE IF NOT EXISTS audit_logs (
    audit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    operation TEXT,
    table_name TEXT,
    field_name TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_level TEXT,
    message TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
