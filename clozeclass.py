import attr

@attr.s(hash=True)
class Cloze:
    cloze_id = attr.ib()
    paragraph = attr.ib()
    source_text = attr.ib()
    source_start = attr.ib()
    cloze_text = attr.ib()
    answer_text = attr.ib()
    answer_start = attr.ib()
    constituency_parse = attr.ib()
    root_label = attr.ib()
    answer_type = attr.ib()
    question_text = attr.ib()