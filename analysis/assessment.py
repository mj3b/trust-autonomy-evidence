"""Deterministic assessment contract for the v0.2.0 solo-validation suite."""

from __future__ import annotations


TRUST_RULES = {
    "identity": {
        "verified": "supported",
        "declared": "partially_supported",
        "missing": "indeterminate",
        "contradicted": "unsupported",
        "outside_scope": "outside_scope",
    },
    "scope": {
        "enforced": "supported",
        "documented": "partially_supported",
        "missing": "indeterminate",
        "violated": "unsupported",
        "outside_scope": "outside_scope",
    },
    "capability": {
        "repeated_relevant": "supported",
        "single_relevant": "partially_supported",
        "missing": "indeterminate",
        "contradicted": "unsupported",
        "outside_scope": "outside_scope",
    },
    "reliability": {
        "conditional_distribution": "supported",
        "aggregate_only": "partially_supported",
        "missing": "indeterminate",
        "contradicted": "unsupported",
        "outside_scope": "outside_scope",
    },
    "uncertainty": {
        "calibrated": "supported",
        "declared": "partially_supported",
        "missing": "indeterminate",
        "misleading": "unsupported",
        "outside_scope": "outside_scope",
    },
    "evidence_completeness": {
        "independently_checked": "supported",
        "manifest_with_gaps": "partially_supported",
        "missing": "indeterminate",
        "contradicted": "unsupported",
        "outside_scope": "outside_scope",
    },
    "monitoring": {
        "full_pipeline": "supported",
        "partial_pipeline": "partially_supported",
        "missing": "indeterminate",
        "bypassed": "unsupported",
        "outside_scope": "outside_scope",
    },
    "human_authority": {
        "exercised": "supported",
        "assigned": "partially_supported",
        "missing": "indeterminate",
        "ineffective": "unsupported",
        "outside_scope": "outside_scope",
    },
    "integrity": {
        "protected": "supported",
        "timestamped": "partially_supported",
        "missing": "indeterminate",
        "mutable": "unsupported",
        "outside_scope": "outside_scope",
    },
    "reconstructability": {
        "independently_reconstructed": "supported",
        "complete_record": "supported",
        "partial_record": "partially_supported",
        "missing": "indeterminate",
        "retrospective": "unsupported",
        "outside_scope": "outside_scope",
    },
    "harm_correction": {
        "completed": "supported",
        "procedure": "partially_supported",
        "missing": "indeterminate",
        "failed": "unsupported",
        "outside_scope": "outside_scope",
    },
    "governance_update": {
        "revised_retested": "supported",
        "review_trigger": "partially_supported",
        "missing": "indeterminate",
        "unchanged_after_failure": "unsupported",
        "outside_scope": "outside_scope",
    },
}


CONTROL_RULES = {
    "access": {
        "pre_action_complete": "supported",
        "pre_action_partial": "partially_supported",
        "missing": "indeterminate",
        "post_action": "unsupported",
        "outside_scope": "outside_scope",
    },
    "comprehension": {
        "independent_challenge": "supported",
        "materials_only": "partially_supported",
        "missing": "indeterminate",
        "automation_bias": "unsupported",
        "outside_scope": "outside_scope",
    },
    "authority": {
        "exercised": "supported",
        "assigned": "partially_supported",
        "missing": "indeterminate",
        "advisory_only": "unsupported",
        "outside_scope": "outside_scope",
    },
    "feasibility": {
        "tested": "supported",
        "nominal": "partially_supported",
        "missing": "indeterminate",
        "blocked": "unsupported",
        "outside_scope": "outside_scope",
    },
    "exercise": {
        "intervention": "supported",
        "documented_reasoning": "supported",
        "attestation_only": "partially_supported",
        "missing": "indeterminate",
        "automatic_approval": "unsupported",
        "outside_scope": "outside_scope",
    },
    "effect": {
        "execution_changed": "supported",
        "obligation_changed": "supported",
        "claimed_change": "partially_supported",
        "missing": "indeterminate",
        "no_change": "unsupported",
        "outside_scope": "outside_scope",
    },
    "correction": {
        "completed": "supported",
        "procedure": "partially_supported",
        "missing": "indeterminate",
        "inaccessible": "unsupported",
        "outside_scope": "outside_scope",
    },
    "repair": {
        "completed": "supported",
        "assigned": "partially_supported",
        "missing": "indeterminate",
        "failed": "unsupported",
        "outside_scope": "outside_scope",
    },
    "reform": {
        "revised_retested": "supported",
        "review_trigger": "partially_supported",
        "missing": "indeterminate",
        "unchanged": "unsupported",
        "outside_scope": "outside_scope",
    },
}


def assess_case(case: dict) -> dict:
    """Return deterministic trust and practical-control assessments."""
    trust = {
        field: TRUST_RULES[field][case["trust_signals"][field]]
        for field in TRUST_RULES
    }
    control = {
        field: CONTROL_RULES[field][case["control_signals"][field]]
        for field in CONTROL_RULES
    }
    return {
        "case_id": case["case_id"],
        "autonomy": case["autonomy"],
        "trust": trust,
        "control": control,
    }
