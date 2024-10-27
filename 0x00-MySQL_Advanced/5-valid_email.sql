-- Write a SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed.

CREATE trigger resetAttr
AFTER UPDATE ON users
FOR EACH ROW
    IF OLD.email <> NEW.email THEN
        UPDATE users
        SET valid_email = 0
        WHERE id = OLD.id;
    ELSE
        UPDATE users
        SET valid_email = 1
        WHERE id = OLD.id;
    END IF;

