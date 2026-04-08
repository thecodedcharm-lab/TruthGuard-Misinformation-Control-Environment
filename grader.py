def grade_easy(posts_handled):
    if posts_handled >= 5:
        return 1.0
    return posts_handled / 5


def grade_medium(posts_handled):
    if posts_handled >= 10:
        return 1.0
    return posts_handled / 10


def grade_hard(posts_handled):
    if posts_handled >= 20:
        return 1.0
    return posts_handled / 20
