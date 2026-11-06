import a_mad_libs_generator
mad = a_mad_libs_generator

adjective = "TESTadjective"
noun = "TESTnoun"
verb = "TESTverb"
place = "testPLACE"

def test_stories_count():
    check = mad.get_story(adjective, noun, verb, place)
    assert len(check) == 3

def test_noun_verb_adjective_place_insertion(monkeypatch):
    user_inputs = iter([noun, verb, adjective, place])
    monkeypatch.setattr('builtins.input', lambda _: next(user_inputs))
    check = mad.mad_libs()
    assert noun.lower() in check
    assert verb.lower() in check
    assert adjective.lower() in check
    assert place.lower().capitalize() in check

def test_story_is_random(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "test")
    picked_stories = set()
    for _ in range (100):
        check = mad.mad_libs()
        picked_stories.add(check)
    assert len(picked_stories) == 3

def test_checking_alpha_strip():
    assert mad.is_word_valid("  test  ") == True

def test_checking_alpha_one_word_with_only_letters():
    assert mad.is_word_valid("444") == False
    assert mad.is_word_valid("a") == False
    assert mad.is_word_valid(" ") == False
    assert mad.is_word_valid("@#$%^&") == False

def test_play_again_yes(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "yes")
    check = mad.play_again()
    assert check

def test_play_again_no(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "no")
    check = mad.play_again()
    assert check == False

def test_play_again_other(monkeypatch):
    user_answers = ["test", "no"]
    user_answers = iter(user_answers)
    monkeypatch.setattr('builtins.input', lambda _: next(user_answers))
    check = mad.play_again()
    assert check == False
