-- A script that creates a stored procedure "ComputeAverageScoreForUser"...
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    -- Compute total score for the user
    SELECT SUM(score)
    INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Compute total number of projects for the user
    SELECT COUNT(*)
    INTO total_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Compute and store the average score for the user
    IF total_projects > 0 THEN
        UPDATE users
        SET average_score = total_score / total_projects
        WHERE id = user_id;
    ELSE
        UPDATE users
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END;
//

DELIMITER ;
