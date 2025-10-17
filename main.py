from linked_list import LinkedList

def main():
    """
    Demonstrate the LinkedList functionality with employee ID management scenario.
    """
    print("=== Employee ID Management System ===")
    print("Using Linked Lists with Recursive Operations\n")
    
    # 1) Create a LinkedList instance
    employee_roster = LinkedList()
    print("📋 Created an empty employee roster")
    
    # 2) Insert some sample employee IDs
    print("\n🔢 Adding employee IDs to the roster:")
    
    # Insert IDs at the front (most recent hires first)
    employee_ids = [101, 205, 150, 320, 275]
    
    print("Inserting at front:", end=" ")
    for emp_id in employee_ids:
        employee_roster.insert_at_front(emp_id)
        print(f"{emp_id}", end=" ")
    print()
    
    # Insert one ID at the end (transfer from another department)
    print("Inserting 999 at end (transfer)")
    employee_roster.insert_at_end(999)
    
    # 3) Display the list to verify insertion
    print("\n📊 Current employee roster:")
    employee_roster.display()
    
    # 4) Call recursive_sum and print the result
    print("\n🧮 Calculating total of all employee IDs (recursive sum):")
    total_sum = employee_roster.recursive_sum()
    print(f"Total sum of all employee IDs: {total_sum}")
    
    # 5) Call recursive_search with different targets and print results
    print("\n🔍 Searching for specific employee IDs:")
    
    search_targets = [150, 999, 500]
    for target in search_targets:
        found = employee_roster.recursive_search(target)
        status = "✅ Found" if found else "❌ Not found"
        print(f"Employee ID {target}: {status}")
    
    # 6) Call recursive_reverse, then display the reversed list
    print("\n🔄 Reversing the employee roster (in-place):")
    print("Before reverse:")
    employee_roster.display()
    
    employee_roster.recursive_reverse()
    
    print("After reverse:")
    employee_roster.display()
    
    # Demonstrate with empty list
    print("\n🆕 Testing with empty roster:")
    empty_roster = LinkedList()
    print("Empty roster display:")
    empty_roster.display()
    print(f"Sum of empty roster: {empty_roster.recursive_sum()}")
    print(f"Search for 100 in empty roster: {empty_roster.recursive_search(100)}")
    
    print("\n✨ All operations completed successfully!")

if __name__ == "__main__":
    main()