import matplotlib.pyplot as plt

def generate_gantt_chart(week_number, tasks, filename):
    """
    Create and save a Gantt chart figure for a given set of tasks.
    Each task is a dict with:
      {
        'name': str,
        'start': int,  # starting week
        'end': int     # ending week (inclusive or exclusive as you see fit)
      }
    """
    fig, ax = plt.subplots(figsize=(8, 4))  # Adjust figsize as desired
    
    # Sort tasks so the earliest-starting tasks appear on top
    tasks_sorted = sorted(tasks, key=lambda x: x['start'])
    
    # Prepare y-ticks (reverse order so first task is at top)
    y_labels = [t['name'] for t in tasks_sorted]
    y_positions = range(len(tasks_sorted))
    
    # Plot each task as a horizontal bar
    for i, task in enumerate(tasks_sorted):
        start = task['start']
        duration = task['end'] - task['start']
        ax.barh(i, duration, left=start, height=0.4, align='center')
    
    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels)
    ax.invert_yaxis()  # So the first task is at the top
    ax.set_xlabel('Project Week')
    ax.set_ylabel('Tasks')
    ax.set_title(f"Gantt Chart - End of Week {week_number}")
    
    ax.set_xlim(0, 25)  # If you need to show up to ~Week 25
    ax.set_xticks(range(0, 26))
    
    # Add grid for easier reading
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    
    # Annotate a vertical line to indicate current "end-of-week" checkpoint
    ax.axvline(x=week_number, color='red', linestyle='--', label=f"Week {week_number}")
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()

def get_tasks_for_week(week):
    """
    Return a list of tasks (dicts) that represent
    the incremental changes in the project timeline
    up to the specified 'week'.
    
    Adjust these tasks and the logic as you see fit
    to reflect minor changes from week to week.
    """
    
    # Base tasks (with rough bounding weeks):
    #   1) Literature Review
    #   2) Experimental Setup & Design
    #   3) Preliminary Testing
    #   4) Data Collection & Advanced Testing
    #   5) Analysis & Write-up
    #   6) Final Wrap-Up
    
    # We'll make them evolve over time:
    # - Literature Review might expand slightly up to ~Week 5 if behind schedule
    # - Setup & Design might shift end date from 9 to 10 or 11, etc.
    # - Preliminary Testing might start around Week 6, push from 10 to 11 or 12, etc.
    # - Data Collection might shift from 10–15 to 11–17, etc.
    # - Analysis & Write-up might begin ~Week 10, extend to ~Week 22
    # - Final Wrap-Up might occupy ~Weeks 20–23, and so on.
    
    # *** Feel free to tune these increments as desired. ***
    
    # Default bounding (initial plan):
    lit_rev_start    =  1
    lit_rev_end      =  4
    setup_start      =  3
    setup_end        =  9
    test_start       =  6
    test_end         = 10
    data_start       = 10
    data_end         = 15
    analysis_start   = 10
    analysis_end     = 20
    wrap_start       = 20
    wrap_end         = 23
    
    # We'll do incremental updates based on current week:
    
    if week >= 2:
        # Suppose we realized Literature Review goes slightly longer
        lit_rev_end = max(lit_rev_end, 5)
    
    if week >= 5:
        # Setup & Design found delays in workshop => push end from 9 to 10
        setup_end = 10
    
    if week >= 7:
        # Preliminary Testing also needs a bit more => push end from 10 to 11
        test_end = 11
    
    if week >= 9:
        # Data Collection can't realistically start in full until ~Week 11
        # so shift from (10–15) to (11–16)
        data_start = 11
        data_end   = 16
    
    if week >= 10:
        # Realize Analysis & Write-up can run partially in parallel
        # but might need to extend to 21
        analysis_end = 21
    
    if week >= 13:
        # Additional complexity discovered => Data Collection extends to 17
        data_end = 17
    
    if week >= 16:
        # Laser method approach => need 1 more week for analysis => 22
        analysis_end = 22
    
    if week >= 20:
        # Final wrap-up might need an extra week => shift from 20–23 to 20–24
        wrap_end = 24
    
    # The tasks as of the current week:
    tasks = [
        {'name': 'Literature Review',                'start': lit_rev_start,  'end': lit_rev_end},
        {'name': 'Experimental Setup & Design',      'start': setup_start,    'end': setup_end},
        {'name': 'Preliminary Testing',              'start': test_start,     'end': test_end},
        {'name': 'Data Collection & Adv Testing',    'start': data_start,     'end': data_end},
        {'name': 'Analysis & Write-up',              'start': analysis_start, 'end': analysis_end},
        {'name': 'Final Wrap-Up',                    'start': wrap_start,     'end': wrap_end},
    ]
    
    return tasks

def main():
    for wk in range(1, 24):  # Weeks 1 through 23
        tasks_for_wk = get_tasks_for_week(wk)
        filename = f"gantt_week_{wk}.png"
        generate_gantt_chart(wk, tasks_for_wk, filename)
        print(f"Saved: {filename}")

if __name__ == "__main__":
    main()
