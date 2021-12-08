import unittest

from pydantic import ValidationError

from app.domain.exams.review import Review


class TestReview(unittest.TestCase):
    def test_review_attributes(self):
        review = Review(grade=10, reviewer_rol='creator', reviewer_id='reviewer@example.com')

        self.assertIsInstance(review.grade, int)
        self.assertIsInstance(review.user, str)
        self.assertIsInstance(review.role, str)

    def test_review_grade_should_be_greater_than_zero(self):
        def review_grade_not_positive(grade: int):
            Review(grade=grade, reviewer_rol='creator', reviewer_id='reviewer@example.com')

        self.assertRaises(ValidationError, review_grade_not_positive, 0)
        self.assertRaises(ValidationError, review_grade_not_positive, -1)

    def test_review_grade_should_be_less_than_or_equal_ten(self):
        def review_grade_greater_than_ten(grade: int):
            Review(grade=grade, reviewer_rol='creator', reviewer_id='reviewer@example.com')

        self.assertRaises(ValidationError, review_grade_greater_than_ten, 11)


if __name__ == '__main__':
    unittest.main()
