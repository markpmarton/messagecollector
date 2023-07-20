INSERT INTO app_user(customerId, name) VALUES (1, 'Test User Name');
INSERT INTO app_user(customerId, name) VALUES (2, 'Test User 2 Name');
INSERT INTO type(name) VALUES ('Type1');
INSERT INTO type(name) VALUES ('Type2');
INSERT INTO message(type_id, app_user_id, amount) VALUES (
  (SELECT uuid FROM type WHERE name='Type1'),
  (SELECT uuid FROM app_user WHERE name='Test User Name'),
  '3.19'
);
INSERT INTO message(type_id, app_user_id, amount) VALUES (
  (SELECT uuid FROM type WHERE name='Type2'),
  (SELECT uuid FROM app_user WHERE name='Test User Name'),
  '0.511'
);
INSERT INTO message(type_id, app_user_id, amount) VALUES (
  (SELECT uuid FROM type WHERE name='Type1'),
  (SELECT uuid FROM app_user WHERE name='Test User 2 Name'),
  '1.1'
);
INSERT INTO message(type_id, app_user_id, amount, received_at) VALUES (
  (SELECT uuid FROM type WHERE name='Type2'),
  (SELECT uuid FROM app_user WHERE name='Test User 2 Name'),
  '6.9',
  '2001-01-01 01:01:01.00'
);
INSERT INTO message(type_id, app_user_id, amount, received_at) VALUES (
  (SELECT uuid FROM type WHERE name='Type2'),
  (SELECT uuid FROM app_user WHERE name='Test User 2 Name'),
  '0.3',
  '3001-01-01 01:03:01.00'
);
