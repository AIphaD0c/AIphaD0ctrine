# Agents

## Operating principle

Agents may propose. The orchestration layer decides.

No single generative model should be allowed to silently redefine identity, consent, safety limits, or canon.

## Agent registry

| Agent | Input | Output | Failure mode to guard against |
|---|---|---|---|
| Vision | video frames | visual features | confusing spectacle with presence |
| Audio | stems / mix | temporal audio features | over-weighting loudness |
| Motion | pose / IMU / video | body state | unnatural hands or impossible motion |
| Audience | crowd media | response model | random crowd behavior |
| Dramaturgy | fused timeline | beat map | generic trailer structure |
| Identity | calibration + beat map | identity state | coercive or deceptive framing |
| Memory | session events | memory salience map | false autobiographical claims |
| Safety | all states | constraints / aborts | excessive intensity or disorientation |
| Director | all analyses | runtime cues | cinematic camera logic replacing embodiment |
| Embodiment | participant + runtime | body ownership cues | latency-induced detachment |
| Stadium | cues + participant action | environment response | non-causal spectacle |

## Agent output rules

Every agent output must include:

- confidence
- source provenance
- timestamp or time interval
- assumptions
- safety relevance
- deterministic fallback

## Human authority

A human project owner retains authority over:

- canon
- release decisions
- public claims
- use of real identities
- data licensing
- safety thresholds
- final experience approval
