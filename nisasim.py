#!/usr/bin/env python3
# encoding: utf-8
"""積み立てNISAの運用シミュレーションCLI。"""

from __future__ import annotations

import argparse


def simulate(monthly_contribution: float, annual_return_percent: float, years: int) -> tuple[float, float, float]:
    """毎月積み立て・複利運用した元本・運用収益・最終金額を返す。"""
    months = years * 12
    monthly_rate = annual_return_percent / 100 / 12
    balance = 0.0

    for _ in range(months):
        balance *= 1 + monthly_rate
        balance += monthly_contribution

    principal = monthly_contribution * months
    profit = balance - principal

    return principal, profit, balance


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="積み立てNISAの運用シミュレーション")
    parser.add_argument("monthly_contribution", type=float, help="毎月の積立金額（円）")
    parser.add_argument("annual_return", type=float, help="予定利回り（年率、%%）")
    parser.add_argument("years", type=int, help="運用年数")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    principal, profit, result = simulate(args.monthly_contribution, args.annual_return, args.years)
    print(f"{principal:.0f}\t{profit:.0f}\t{result:.0f}")


if __name__ == "__main__":
    main()
