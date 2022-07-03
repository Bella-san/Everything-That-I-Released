init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="watching_animeBELLA",
            category=["be right back"],
            prompt="I'm going to watch anime",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label watching_animeBELLA:
    m 1esb "You're going to watch anime? Okay!"
    m 1hua "Maybe when I cross over, we can watch anime together~"
    m "I'll be waiting for you."

$ mas_idle_mailbox.send_idle_cb("watching_animeBELLA_callback")
return "idle"

label watching_animeBELLA_callback:
    m 7wuo "Oh! You're back!"
    m 3hua "Hello, [player]~"
    m 1eua "What should we do next?"
return
