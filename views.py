def show_exam_result(request, course_id, submission_id):

    submission = get_object_or_404(Submission, pk=submission_id)

    choices = submission.choices.all()

    total = choices.count()
    score = 0

    for choice in choices:
        if choice.is_correct:
            score += 1

    context = {
        'score': score,
        'total': total,
        'choices': choices
    }

    return render(request, 'exam_result_bootstrap.html', context)
