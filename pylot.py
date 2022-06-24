def patches() -> list:
    """ Patches for Unit Tests """
    test_cases = [
        # Generic Fail
        [
            (
                'protobuf_utils.load_build_description_from_yaml',
                ['/home'], {},
                (),
            ),
            ("master", [], {}, "master"),
            ("test-repo", [], {}, "test-repo"),
            (
                'docker_utils.get_client', [], {},
                (),
            ),
        ],
        # Successful
    ]
    return test_cases


def test_results() -> list:
    """Test Results for Unit Tests."""
    test_results = [
        # Generic failing build.
        ('band'),
    ]
    return test_results

print(list(zip(patches(), test_results())))