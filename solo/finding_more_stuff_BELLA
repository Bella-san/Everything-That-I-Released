init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="finding_more_stuff_BELLA",
            category=["be right back"],
            prompt="I'm going to find more spritepacks/submods for you on the MAS subreddit.",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label finding_more_stuff_BELLA:
    m 4hub "How exciting!"
    m 1eua "I'll be looking forward to it then~"
    m 5hua "See you~"
$ mas_idle_mailbox.send_idle_cb("finding_more_stuff_BELLA_callback")
return "idle"

label finding_more_stuff_BELLA_callback:
    m 3hub "Welcome back, [player]!"
    m 2etb "Did you find any new stuff?{nw}"
menu:
    m "Did you find any new stuff?{fast}"

    "Yes":
        m 3hua "That's nice, [player]!"
        m 1eua "I'll be looking forward to it then~"

    "No":
        m 1ekd "Aww..."
        m 2ekc "..."
        m 1eka "It's okay, [player]."
        m 1esa "Maybe you'll find more tomorrow!"
        m 3hub "It's the thought that counts anyways~"
return
