import unittest

from app.domain.exams.review import Review
from app.domain.exams.submitted_exam import SubmittedExam
from tests.examples.submitted_exam_example import SubmittedExamExample


class TestRevisedExamUseCase(unittest.TestCase):
    def test_revised_exam_attributes(self):
        submitted_exam = SubmittedExamExample().build()
        review = Review(grade=10, role='creator', user='reviewer@example.com')

        revised_exam = submitted_exam.correct(review)

        self.assertIsInstance(revised_exam.submitted_exam, SubmittedExam)
        self.assertIsInstance(revised_exam.review, Review)


if __name__ == '__main__':
    unittest.main()
