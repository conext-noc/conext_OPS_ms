-- SELECT * FROM db_api_plans;
-- SELECT * FROM db_api_clients;
-- SELECT * FROM db_api_alarms;
-- SELECT * FROM db_api_ports;
SELECT * FROM db_api_oltpasswords;
-- UPDATE db_api_oltpasswords SET password = 'bhSQ#b$2vd1$' WHERE cred_id = 3;

-- 
-- INSERT INTO db_api_oltpasswords (user_name, password)
-- VALUES ('huawei', 'Tec#2023X$'),
-- ('admin_1', 'bhSQ#b$2vd$1'),
-- ('root_oz', '7t#TNXp$v@6v') 
-- 
-- 
-- UPDATE db_api_clients SET contract='0000006485' WHERE contract='6485'
-- UPDATE db_api_plans SET plan_name = 'OZ_DEDICADO_5_IP' WHERE plan_name = 'OZ_DEDICADO_IP_5'
-- UPDATE db_api_ SET plan_name = 'OZ_DEDICADO_5_IP' WHERE plan_name = 'OZ_DEDICADO_IP_5'
-- 
-- 
-- delete from db_api_clients
-- delete from db_api_plans
-- delete from db_api_clients WHERE contract='9000000016';
-- delete from db_api_ports WHERE olt=2;
-- delete from db_api_plans