CREATE FUNCTION create_superadmin() RETURNS integer AS $$

DECLARE
    valueStorageId integer;  
BEGIN
   select nextval('storage_seq') into valueStorageId;
   INSERT INTO value_storage VALUES (valueStorageId);
   INSERT INTO setting_value VALUES (valueStorageId, 'ENABLE','permission/application/superadmin');
   INSERT INTO users VALUES (nextval('user_seq'), NULL, '12345678', '12345678', NULL, 'superadmin', valueStorageId, NULL, false, NULL, 'C', 'Ezuce123', true);
    RETURN 0;
END;
$$ LANGUAGE plpgsql;
select create_superadmin();
