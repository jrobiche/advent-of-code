#!/usr/bin/env python3

from collections import namedtuple

Rate = namedtuple("Rate", ["value", "length"])


def rate_complement(rate):
    complement_value = (1 << rate.length) - 1
    complement_value &= ~rate.value
    return Rate(complement_value, rate.length)


def most_common_value_in_bit_position(report, position):
    report_length = len(report)
    half_report_length = float(report_length) / 2
    one_count = sum(1 for entry in report if entry[position] == "1")
    if one_count > half_report_length:
        return "1"
    if one_count < half_report_length:
        return "0"
    return None


def get_gamma_rate(report=None, epsilon_rate=None):
    if epsilon_rate:
        return rate_complement(epsilon_rate)
    rate_value = 0
    rate_length = len(report[0])
    for bit_position in range(rate_length):
        most_common_value = most_common_value_in_bit_position(
            report, bit_position)
        rate_value <<= 1
        if most_common_value == "1":
            rate_value += 1
    return Rate(rate_value, rate_length)


def get_epsilon_rate(report=None, gamma_rate=None):
    if gamma_rate:
        return rate_complement(gamma_rate)
    rate_value = 0
    rate_length = len(report[0])
    for bit_position in range(rate_length):
        most_common_value = most_common_value_in_bit_position(
            report, bit_position)
        rate_value <<= 1
        if most_common_value == "0":
            rate_value += 1
    return Rate(rate_value, rate_length)


def get_power_consumption(gamma_rate, epsilon_rate):
    return gamma_rate.value * epsilon_rate.value


def get_oxygen_generator_rating(report):
    def bit_criteria(report_entry):
        if most_common_value is None or most_common_value == "1":
            return report_entry[bit_position] == "1"
        return report_entry[bit_position] == "0"

    report_entries = report
    rate_length = len(report[0])
    for bit_position in range(0, rate_length):
        most_common_value = most_common_value_in_bit_position(
            report_entries, bit_position)
        report_entries = list(filter(bit_criteria, report_entries))
        if len(report_entries) == 1:
            rate_value = int(report_entries[0], base=2)
            return Rate(rate_value, rate_length)
    return None


def get_co2_scrubber_rating(report):
    def bit_criteria(report_entry):
        if most_common_value is None or most_common_value == "1":
            return report_entry[bit_position] == "0"
        return report_entry[bit_position] == "1"

    report_entries = report
    rate_length = len(report[0])
    for bit_position in range(0, rate_length):
        most_common_value = most_common_value_in_bit_position(
            report_entries, bit_position)
        report_entries = list(filter(bit_criteria, report_entries))
        if len(report_entries) == 1:
            rate_value = int(report_entries[0], base=2)
            return Rate(rate_value, rate_length)
    return None


def get_life_support_rating(oxygen_generator_rating, co2_scrubber_rating):
    return oxygen_generator_rating.value * co2_scrubber_rating.value


def main():
    # input_file = "test_input.txt"
    input_file = "input.txt"

    with open(input_file, encoding="utf-8") as fp:
        report = [line.strip() for line in fp.readlines()]

    print("=== Part 1 ===")
    gamma_rate = get_gamma_rate(report=report)
    epsilon_rate = get_epsilon_rate(gamma_rate=gamma_rate)
    power_consumption = get_power_consumption(gamma_rate, epsilon_rate)
    print(f"Power consumption: {power_consumption}")

    print("=== Part 2 ===")
    oxygen_generator_rating = get_oxygen_generator_rating(report)
    co2_scrubber_rating = get_co2_scrubber_rating(report)
    life_support_rating = get_life_support_rating(oxygen_generator_rating,
                                                  co2_scrubber_rating)
    print(f"Life support rating: {life_support_rating}")


if __name__ == "__main__":
    main()
