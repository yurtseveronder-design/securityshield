"""Threat detectors.

A heuristic scorer, plus a prompt-injection guardrail, that turn
normalized text into a risk signal.
"""

from ai_sentinel.core.heuristic_scorer import HeuristicResult, HeuristicScorer
from ai_sentinel.detectors.injection import InjectionGuardrail, InjectionScanResult, PatternLog

__all__ = [
    "HeuristicResult",
    "HeuristicScorer",
    "InjectionGuardrail",
    "InjectionScanResult",
    "PatternLog",
]
