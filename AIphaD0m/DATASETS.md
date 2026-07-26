# Dataset strategy

## Principle

AIphaD0m must not treat public availability as permission.

Every dataset, clip, recording, scan, motion capture, voice, face, and performance reference must have documented rights and permitted uses.

## Candidate research datasets

The following categories are relevant for research and prototyping, subject to their current licenses and access terms:

- egocentric video for body and gaze understanding
- synchronized ego/exocentric video for performer reconstruction
- audio-visual music performance datasets
- multi-camera performance datasets
- crowd-motion and event-audio datasets
- spatial-audio and room-response datasets

Potential research references include Ego4D, Ego-Exo4D, URMP, MUSIC-AVQA, MusiQAl, and other appropriately licensed collections. Their inclusion here is not a license grant. Terms must be verified before use.

## Preferred proprietary dataset

The long-term core dataset should be purpose-recorded and rights-clean.

Recommended capture package:

- performer head-mounted or chest-mounted cameras
- synchronized stage cameras
- hand and instrument close-ups
- inertial measurement units
- multitrack audio and ambience
- crowd microphones
- lighting and show-control logs
- stage geometry
- participant consent and performer releases

## Provenance record

Every asset should have a sidecar record containing:

- source
- rights holder
- license
- permitted use
- prohibited use
- attribution requirement
- expiry or revocation conditions
- transformations performed
- model-training permission
- public-release permission

## Prohibited ingestion

Do not ingest:

- scraped private media
- unauthorized concert recordings for model training
- biometric data without explicit consent
- voice or face data used to imitate a real person without authorization
- datasets whose terms are incompatible with redistribution or intended use
