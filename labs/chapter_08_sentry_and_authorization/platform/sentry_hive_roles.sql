-- Historical Sentry/Hive illustration from the theory chapter.
-- PLATFORM-DEPENDENT: requires a compatible Sentry/Hive environment.
CREATE ROLE course_reader;
GRANT SELECT ON TABLE teaching.public_notes TO ROLE course_reader;
GRANT ROLE course_reader TO GROUP students;
