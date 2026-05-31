import json

CHECKLIST = [
    {"item": "Data protection policy in place", "done": False},
    {"item": "Access controls implemented", "done": False},
    {"item": "Incident response plan documented", "done": False},
    {"item": "Regular security training conducted", "done": False},
    {"item": "Data processing agreements signed", "done": False}
]

SAVE_FILE = 'checklist_status.json'

def load_status():
    try:
        with open(SAVE_FILE, 'r') as f:
            return json.load(f)
    except Exception:
        return CHECKLIST.copy()

def save_status(status):
    with open(SAVE_FILE, 'w') as f:
        json.dump(status, f, indent=2)

def show_checklist(status):
    print("\nCompliance Checklist:")
    for idx, item in enumerate(status):
        mark = '[x]' if item['done'] else '[ ]'
        print(f"{idx+1}. {mark} {item['item']}")

def main():
    status = load_status()
    while True:
        show_checklist(status)
        print("\nEnter number to toggle, 'r' to report, 'q' to quit:")
        choice = input('> ').strip()
        if choice == 'q':
            save_status(status)
            break
        elif choice == 'r':
            done = sum(1 for i in status if i['done'])
            print(f"\nCompleted: {done}/{len(status)} items.")
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(status):
                status[idx]['done'] = not status[idx]['done']
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
