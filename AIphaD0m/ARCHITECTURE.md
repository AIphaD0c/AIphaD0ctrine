# Architecture

## System overview

AIphaD0m is designed as a multi-agent pipeline with explicit boundaries between observation, interpretation, generation, embodiment, and rendering.

```text
Input sources
  ├─ reference performances
  ├─ licensed music and stems
  ├─ performer motion
  ├─ crowd behavior
  ├─ environmental scans
  └─ participant calibration
          │
          ▼
Perception layer
  ├─ Vision Agent
  ├─ Audio Agent
  ├─ Motion Agent
  └─ Audience Agent
          │
          ▼
Interpretation layer
  ├─ Dramaturgy Agent
  ├─ Identity Agent
  ├─ Memory Agent
  └─ Safety Agent
          │
          ▼
Direction layer
  ├─ Director Agent
  ├─ Embodiment Agent
  └─ Stadium Agent
          │
          ▼
Generation and runtime
  ├─ Scene generator
  ├─ Animation / motion synthesis
  ├─ Spatial audio renderer
  ├─ Haptic controller
  └─ Engine adapter
          │
          ▼
Participant experience
```

## Core agents

### Vision Agent

Extracts cuts, motion, lighting transitions, stage geometry, performer framing, and crowd visibility.

### Audio Agent

Extracts intensity, rhythm, transients, silence, spectral density, and crowd/music relationships.

### Motion Agent

Models body movement, hand continuity, instrument interaction, breathing, micro-instability, and performer effort.

### Audience Agent

Models crowd density, response latency, collective motion, chanting, phone lights, and performer-to-crowd causality.

### Dramaturgy Agent

Builds a temporal map of anticipation, reveal, expansion, false ending, climax, release, and afterimage.

### Identity Agent

Controls the participant-to-performer identity transition. It must not depend on deception outside the clearly framed experience.

### Memory Agent

Transforms continuous runtime into memory-like salience: compression, omission, repetition, emotional weighting, and residual fragments.

### Safety Agent

Enforces consent, intensity limits, identity boundaries, photoreal-person restrictions, and post-experience reorientation.

### Director Agent

Combines all analyses into shot-free first-person direction: where attention moves, what becomes visible, when the crowd responds, and how reality destabilizes.

### Embodiment Agent

Maintains body ownership through latency control, visual-proprioceptive alignment, believable hands, posture, breathing, and interaction feedback.

### Stadium Agent

Creates a responsive environment whose scale and behavior are causally tied to the participant's actions.

## Data contracts

All agents communicate through typed event structures rather than free-form text alone.

Primary structures:

- `TimelineEvent`
- `SignalFeature`
- `DramaturgyBeat`
- `IdentityState`
- `SafetyConstraint`
- `SessionPlan`

## Engine separation

The core project must remain independent from any one rendering platform.

Adapters may later target:

- Unreal Engine
- Unity
- WebXR
- Apple immersive video
- OpenXR-compatible runtimes
- flat-screen prototype environments

## First technical milestone

Create a deterministic session planner that ingests an analysis timeline and outputs:

- dramaturgical beats
- embodiment intensity
- crowd response targets
- identity transition state
- safety constraints
- engine-neutral runtime cues
