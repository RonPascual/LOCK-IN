# LOCK-IN

## ABOUT
A computer vision application that detects when a phone is visible through a webcam and encourages the user to "lock in" aka stay focused.

## PLANNED FEATURES
* Detect phone in webcam
* Display warning
* Play audio alert
* Open productive websites
* Track distraction statistics

## CODE ORGANIZATION
* `Lock_In.py` combines the app.
* `webcam.py` handles webcam access.
* `detector.py` loads the AI model and detects phones.
* `countdown.py` tracks timing and reset state.
* `ui.py` draws boxes and countdown text.
* `actions.py` handles website-opening actions.
