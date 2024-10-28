from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

###
# create a test each in test_times.py for:
#   two time ranges that do not overlap
#   two time ranges that both contain several intervals each
#   two time ranges that end exactly at the same time when the other starts
# run pytest and see whether all tests are picked up by pytest and whether they pass.
# fix any bugs in times.py the tests may have helped you find.
# Add the new and modified files to the repository, commit them (with a meaningful comment that also includes Answers UCL-COMP0233-24-25/RSE-Classwork#12) and push it to your fork.

def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")
    expected = []
    assert compute_overlap_time(large, short) == expected

def test_multiple_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
                ("2010-01-12 10:38:00", "2010-01-12 10:39:20"),
                ("2010-01-12 10:40:20", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_same_end_start():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 12:15:00")
    expected = []
    assert compute_overlap_time(large, short) == expected