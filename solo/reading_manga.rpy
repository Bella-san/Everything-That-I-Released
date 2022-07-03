init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="reading_mangaBELLA",
            category=["be right back"],
            prompt="I'm going to read manga",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label reading_mangaBELLA:
    m 1etb "You're going to read manga?"
    m 2esa "Alright~"
    m 3hub "I'll be waiting for you."

$ mas_idle_mailbox.send_idle_cb("reading_mangaBELLA_callback")
return "idle"

label reading_mangaBELLA_callback:
    m 1eua "Welcome back, [player]."
return
