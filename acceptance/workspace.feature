@not_run
Feature: Joined Workspace experience
  These scenarios are contracts, not implemented or executed step definitions.

  @CREATE-01
  Scenario: Global plus preserves the working context
    Given a document is open with unsent writing
    When the user opens global plus
    Then the centered composer opens without changing route or losing the draft

  @CREATE-02
  Scenario: Escape closes the innermost surface
    Given a menu is open inside the creation composer
    When the user presses Escape
    Then only the menu closes and the composer draft remains

  @CREATE-03
  Scenario: New task opens its actual shelf
    Given a valid unassigned task draft exists
    When the user submits it once
    Then one canonical task is saved and its shelf opens without starting an arbitrary coworker

  @CREATE-04
  Scenario: Creation retries do not duplicate work
    Given a task save receipt was lost after persistence
    When the same submission identity is retried
    Then the existing task is returned and no duplicate activation occurs

  @CREATE-05
  Scenario: Chat opens the selected canonical DM
    Given the user chooses a coworker in Chat mode
    When the user sends a message
    Then the canonical DM opens with exactly one new message

  @CREATE-06
  Scenario: Failed save retains work
    Given a composer contains text and attachments
    When the authoritative save fails
    Then all inputs remain editable and no model is dispatched

  @ASSIGN-01
  Scenario: Fresh tasks are unassigned
    Given a prior task was assigned to a coworker
    When the user starts a fresh global task draft
    Then the assignee is empty unless an explicit default policy says otherwise

  @ASSIGN-02
  Scenario: Assignment is not activation
    Given an unsubmitted draft is open
    When the user chooses another coworker
    Then only draft assignment changes and no message or model call is made

  @ASSIGN-03
  Scenario: Contextual assignment is visible
    Given the user starts work from a coworker DM
    When the new composer opens
    Then the prefilled coworker is visible and can be changed

  @DATE-01
  Scenario: Clear relative due dates are inspectable
    Given the composer has a known local date and timezone
    When the user writes finish this tomorrow
    Then an editable date-only due chip shows the following local calendar date

  @DATE-02
  Scenario: Date mentions are not automatically deadlines
    Given no deadline is selected
    When the user writes summarize tomorrow's meeting notes
    Then the meeting date is not silently committed as the task due date

  @DATE-03
  Scenario: Explicit dates win
    Given the user selected a due date explicitly
    When background inference returns another date
    Then the explicit date remains and the alternative is at most a suggestion

  @DATE-04
  Scenario: Deadlines are not execution schedules
    Given a task has a due date but no start schedule
    When time advances toward the due date
    Then no scheduled execution or calendar event is created solely from that date

  @CAPTURE-01
  Scenario: One browsable capture library
    Given permitted captures have stable original identities
    When the user opens Captures from the global command
    Then the same library is displayed without duplicating source files

  @CAPTURE-02
  Scenario: Capture inspection is source-adjacent
    Given a capture contains original video and annotations
    When the user opens the capture
    Then the shelf shows distinct originals and annotations with available timestamps

  @CAPTURE-03
  Scenario: Capture-to-task handoff preserves evidence
    Given a permitted capture is selected
    When the user creates a task from it
    Then the saved task references exact capture evidence and original files remain unchanged

  @CAPTURE-04
  Scenario: Capture reads respect scope
    Given a capture is outside the current actor's authority
    When the actor searches or guesses its media path
    Then neither content nor private metadata is returned

  @CAPTURE-05
  Scenario: Malformed media paths are rejected
    Given a manifest contains a path escaping its capture directory
    When the media is requested
    Then the request is denied without serving the outside file

  @POLICY-01
  Scenario: Exact approval cannot authorize changed content
    Given one payload and destination were approved
    When the actor changes the payload or account
    Then execution is denied and a new approval is required

  @POLICY-02
  Scenario: Approval claims are single-use
    Given one approval is pending execution
    When two workers try to claim it concurrently
    Then only one claim can authorize execution

  @POLICY-03
  Scenario: Changed access invalidates waiting work
    Given an action waits under a captured capability policy
    When the applicable access is revoked
    Then the old approval cannot authorize that action

  @POLICY-04
  Scenario: Alternative tools cannot bypass policy
    Given an external effect is denied
    When the agent attempts it through voice browser shell or another connector
    Then the same consequence remains denied

  @POLICY-05
  Scenario: Unknown is not failure
    Given a provider may have accepted an action before a timeout
    When the run recovers
    Then the action remains unknown pending reconciliation rather than being blindly repeated

  @VOICE-01
  Scenario: Named calls use the named identity
    Given a coworker has a configured identity version
    When the user starts a call and asks who is speaking
    Then the response uses that coworker identity and the receipt identifies the same version

  @VOICE-02
  Scenario: Missing identity fails clearly
    Given the requested coworker identity cannot be resolved
    When the user starts a named call
    Then the call fails explicitly rather than presenting a generic assistant as that coworker

  @VOICE-03
  Scenario: Text and voice share context
    Given a canonical discussion contains a synthetic fact
    When the user changes to voice and asks about it
    Then the same authorized conversation context is used without a competing chat history

  @VOICE-04
  Scenario: Dictation is not submission
    Given the user dictates into an unsent draft
    When transcription completes
    Then text is inserted into that draft and no task message or external action is submitted

  @VOICE-05
  Scenario: Minimize and End differ
    Given a voice call is connected
    When the user minimizes and then explicitly ends it
    Then minimizing preserves the call while End closes audio and preserves unresolved actions

  @VOICE-06
  Scenario: Voice uses normal action controls
    Given a voice turn proposes an operation requiring approval
    When the user reviews its exact operation
    Then the existing action approval and receipt path applies without broader voice permissions

  @RELEASE-01
  Scenario: Private material is not application source
    Given an operational checkout contains user data and restricted vendor files
    When a public release candidate is extracted
    Then only rights-cleared reviewed files and synthetic fixtures enter the candidate

  @RELEASE-02
  Scenario: Preparation cannot masquerade as shipping
    Given the public package contains documentation but no application
    When preparation checks pass
    Then application readiness remains blocked and no installability claim is made
