USE student_pipeline;
-- ============================================
-- TOP STUDENTS
-- ============================================
SELECT * FROM performance_summary
ORDER BY average_marks DESC
LIMIT 5;

-- ============================================
-- LOW PERFORMERS
-- ============================================

SELECT * FROM performance_summary
WHERE performance = 'Needs Improvement';

-- ============================================
-- ATTENDANCE VS PERFORMANCE
-- ============================================

SELECT performance, AVG(attendance_percentage)
FROM performance_summary
GROUP BY performance;