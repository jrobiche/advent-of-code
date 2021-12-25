DEFAULT_DIGIT_SEGMENTS = [
    # zero
    {"a", "b", "c", "e", "f", "g"},
    # one
    {"c", "f"},
    # two
    {"a", "c", "d", "e", "g"},
    # three
    {"a", "c", "d", "f", "g"},
    # four
    {"b", "c", "d", "f"},
    # five
    {"a", "b", "d", "f", "g"},
    # six
    {"a", "b", "d", "e", "f", "g"},
    # seven
    {"a", "c", "f"},
    # eight
    {"a", "b", "c", "d", "e", "f", "g"},
    # nine
    {"a", "b", "c", "d", "f", "g"},
]


def parse_file(input_file):
    with open(input_file, "r", encoding="utf-8") as fp:
        file_lines = [line.strip() for line in fp.readlines()]
    parsed_lines = []
    for line in file_lines:
        partitioned_entry = line.partition(" | ")
        unique_patterns = partitioned_entry[0].split(" ")
        output_value = partitioned_entry[-1].split(" ")
        parsed_lines.append((unique_patterns, output_value))
    return parsed_lines


def decode_value(value, encoding_map):
    """
    Given a value as a string of segments encoded using the given encoding map,
    return the decoded value as an integer.
    """
    decoded_value = 0

    for encoded_segments in value:
        decoded_segments = {
            encoding_map[segment]
            for segment in encoded_segments
        }

        decoded_digit = DEFAULT_DIGIT_SEGMENTS.index(decoded_segments)

        decoded_value *= 10
        decoded_value += decoded_digit

    return decoded_value


def get_encoding_map(encoded_signal_patterns):
    # for each original letter (key), assign a set of possible letters that
    # the equivalent encoded letter could be (value)
    #
    # any letters that are determined to not be a possible encoded version
    # of the original letter (key) will be removed from the set of possible
    # encoded letters (value)
    #
    # example result: {"a": {"c"}} means that the 'a' segment
    # (top-most horizontal segment) in the default encoding maps to
    # the 'c' segment in the new encoding
    segment_encoding = {
        "a": {"a", "b", "c", "d", "e", "f", "g"},
        "b": {"a", "b", "c", "d", "e", "f", "g"},
        "c": {"a", "b", "c", "d", "e", "f", "g"},
        "d": {"a", "b", "c", "d", "e", "f", "g"},
        "e": {"a", "b", "c", "d", "e", "f", "g"},
        "f": {"a", "b", "c", "d", "e", "f", "g"},
        "g": {"a", "b", "c", "d", "e", "f", "g"},
    }

    # encoded equivalent of DEFAULT_DIGIT_SEGMENTS
    encoded_digit_segments = [set()] * 10

    # create a list of unique encoded numbers
    # only want to decode values once
    encoded_signal_patterns = list(set(encoded_signal_patterns))

    # numbers by length:
    # 0 = {}
    # 1 = {}
    # 2 = {1}
    # 3 = {7}
    # 4 = {4}
    # 5 = {2, 3, 5}
    # 6 = {0, 6, 9}
    # 7 = {8}

    for pattern in encoded_signal_patterns:
        pattern_length = len(pattern)

        if pattern_length == 2:
            digit = 1
        elif pattern_length == 3:
            digit = 7
        elif pattern_length == 4:
            digit = 4
        elif pattern_length == 7:
            digit = 8
        else:
            continue

        pattern_set = set(pattern)

        encoded_digit_segments[digit] = pattern_set

        for original_segment, possible_encodings in segment_encoding.items():
            if original_segment in DEFAULT_DIGIT_SEGMENTS[digit]:
                possible_encodings.intersection_update(pattern_set)
            else:
                possible_encodings -= pattern_set

    i = 0
    encoded_signal_patterns_count = len(encoded_signal_patterns)
    while i < encoded_signal_patterns_count:
        pattern = encoded_signal_patterns[i]
        pattern_length = len(pattern)

        digit = None

        if pattern_length == 5:
            # current digit must be in {2, 3, 5}

            # if the set of encoded letters used to make up 1 and the
            # current digit equals the set of encoded letters in the
            # current digit, then the current digit must be 3
            if encoded_digit_segments[1] \
                    and encoded_digit_segments[1].union(set(pattern)) \
                        == set(pattern):
                digit = 3

            # if the set of encoded letters used to make up 4 and the
            # current digit equals the set of all letters (i.e. the letters
            # used to make up both an encoded and original 8), then the
            # current digit must be 2
            elif encoded_digit_segments[4] \
                    and encoded_digit_segments[4].union(set(pattern)) \
                        == DEFAULT_DIGIT_SEGMENTS[8]:
                digit = 2

            # if the set of encoded letters used to make up 7 and the
            # current digit equals the set of encoded letters in the
            # current digit, then the current digit must be 3
            elif encoded_digit_segments[7] \
                    and encoded_digit_segments[7].union(set(pattern)) \
                        == set(pattern):
                digit = 3

        elif pattern_length == 6:
            # current digit must be in {0, 6, 9}

            # if the set of encoded letters used to make up 1 and the
            # current digit does not equal the set of encoded letters
            # in the current digit, then the current digit must be 6
            if encoded_digit_segments[1] \
                    and encoded_digit_segments[1].union(set(pattern)) \
                        != set(pattern):
                digit = 6

            # if the set of encoded letters used to make up 4 and the
            # current digit equals the set of encoded letters in the
            # current digit, then the current digit must be 9
            elif encoded_digit_segments[4] \
                    and encoded_digit_segments[4].union(set(pattern)) \
                        == set(pattern):
                digit = 9

            # if the set of encoded letters used to make up 7 and the
            # current digit equals the set of all letters (i.e. the letters
            # used to make up both an encoded and original 8), then the
            # current digit must be 6
            elif encoded_digit_segments[7] \
                    and encoded_digit_segments[7].union(set(pattern)) \
                        == DEFAULT_DIGIT_SEGMENTS[8]:
                digit = 6

        if digit is None:
            i += 1
            continue

        pattern_set = set(pattern)

        for original_segment, possible_encodings in segment_encoding.items():
            if original_segment in DEFAULT_DIGIT_SEGMENTS[digit]:
                possible_encodings.intersection_update(pattern_set)
            else:
                possible_encodings -= pattern_set

        if encoded_digit_segments[digit] != pattern_set:
            encoded_digit_segments[digit] = pattern_set
            i = -1

        i += 1

    encoding_map = {}
    for original_letter, encoded_set in segment_encoding.items():
        encoded_letter = encoded_set.pop()
        encoding_map[encoded_letter] = original_letter

    return encoding_map


def solution_1(input_file):
    """
    Return the amount of numbers that are one of the following:
    1, 4, 7, 8
    """
    count = 0

    # if length of signal pattern is:
    # 2 - then digit is 1
    # 3 - then digit is 7
    # 4 - then digit is 4
    # 7 - then digit is 8
    valid_pattern_lengths = [2, 3, 4, 7]

    parsed_entries = parse_file(input_file)

    for entry in parsed_entries:
        output_value = entry[1]
        for signal_pattern in output_value:
            if len(signal_pattern) in valid_pattern_lengths:
                count += 1

    return count


def solution_2(input_file):
    """
    Return the sum of decoded output values for all entries
    """
    output_values_sum = 0

    parsed_entries = parse_file(input_file)

    for unique_signal_patterns, output_value in parsed_entries:
        all_signal_patterns = unique_signal_patterns + output_value
        encoding_map = get_encoding_map(all_signal_patterns)
        decoded_value = decode_value(output_value, encoding_map)
        output_values_sum += decoded_value

    return output_values_sum
