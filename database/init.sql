DROP TABLE IF EXISTS app_user;
CREATE TABLE app_user (
  uuid uuid NOT NULL DEFAULT gen_random_uuid(),
  customerId serial NOT NULL,
  name varchar(255) NOT NULL,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  updated_at timestamp NULL,
  PRIMARY KEY (uuid)
);

DROP TABLE IF EXISTS type;
CREATE TABLE type (
  uuid uuid NOT NULL DEFAULT gen_random_uuid(),
  name varchar(255) NOT NULL,
  PRIMARY KEY (uuid)
);

DROP TABLE IF EXISTS message;
CREATE TABLE message (
  uuid uuid NOT NULL DEFAULT gen_random_uuid(),
  type_id uuid NOT NULL,
  app_user_id uuid NOT NULL,
  amount decimal(10,3) NOT NULL,
  received_at timestamp DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (uuid),
  FOREIGN KEY (type_id) references type(uuid),
  FOREIGN KEY (app_user_id) references app_user(uuid)
);
