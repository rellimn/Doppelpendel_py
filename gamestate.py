from statemachine import StateMachine, State


class GameState(StateMachine):
    starting = State("Starting", initial=True)
    paused = State("Paused")
    running = State("Running")
    ending = State("Ending", final=True)
    #is_stuck = State("Stuck")

    toggle_pause = starting.to(paused) | paused.to(running) | running.to(paused)
    end = starting.to(ending) | paused.to(ending) | running.to(ending) #| is_stuck.to(ending)
    #stuck = is_stuck.

    cont = paused.to(running)
    pause = running.to(paused)
