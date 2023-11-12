# David Liberal
# Assignment: List Election
# Date: Nov 11 2023


# The program must follow this specs
# Add votes from a precinct
# Display all votes from all precincts
# Display vote stats
# Rmeove a precinct and all votes from that precinct
# quit


vote_precinct_mickey = [1515, 800, 200, 78965, 5]
vote_precinct_minnie = [8990, 799, 100, 78888, 3]


def display_votes():
    # Dispaply all votes from all precincts
    count = 0
    print("Precinct No.\tMickey Mouse\tMinnie Mouse")
    for i in vote_precinct_mickey:
        print(f"{count}\t\t{i}\t\t{vote_precinct_minnie[count]}")
        count += 1


def add_votes_precinct():

    precinct_num_option = input(
        "What precinct would like to add votes to? (Will be added if selected precinct does not exist): ")

    # convert the precict option to a integer
    precinct_num = int(precinct_num_option)

    # --------------Append Precinct Value --------------------------

    if precinct_num > len(vote_precinct_mickey):
        new_precinct = input("How many votes did mickey get? ")
        # convert the new precinct vote value to integer and store
        new_precinct = int(new_precinct)
        vote_precinct_mickey.append(new_precinct)

    if precinct_num > len(vote_precinct_minnie):
        new_precinct = input("How many votes did Minnie get? ")
        # convert the new precinct vote value to integer and store
        new_precinct = int(new_precinct)
        vote_precinct_minnie.append(new_precinct)

    # ---------------------Replace Precinct Value-------------------

    # convert the precict option to a integer
    precinct_num = int(precinct_num_option)

    counter = 0

    # change the value from specified precinct no.
    for i in range(len(vote_precinct_mickey)):
        if counter == precinct_num:
            newValue = input(
                f"How many votes did Mickey get for Precinct No.  {precinct_num_option}")
            # convert integer
            newValue = int(newValue)
            vote_precinct_mickey[precinct_num] = newValue
        counter += 1

    # reset counter
    counter = 0

    # change the value from specified precinct no.
    for i in range(len(vote_precinct_minnie)):
        if counter == precinct_num:
            newValue = input(
                f"How many votes did Minnie get for Precinct No.  {precinct_num_option}")
            # convert integer
            newValue = int(newValue)
            vote_precinct_minnie[precinct_num] = newValue
        counter += 1


def display_vote_stats():

    # high - the highest number of votes for that candidate from a single precinct
    j = 0
    current_value = 0
    for i in vote_precinct_mickey:
        if i > current_value:
            current_value = i
        j += 1
    print(f"Mickey Highest Value at No. {j - 2}: {current_value}")

    # reset j counter & current value
    current_value = 0
    j = 0
    for i in vote_precinct_minnie:
        if i > current_value:
            current_value = i
        j += 1
    print(f"Minnie Highest Value at No. {j - 2}: {current_value}")


def remove_precinct():
    remove_Precinct = input("What precinct No. would you like to remove? ")

    # convert input to integer for indexing
    remove_Precinct = int(remove_Precinct)

    # remove precinct value from both lists
    vote_precinct_mickey.remove(vote_precinct_mickey[remove_Precinct])
    vote_precinct_minnie.remove(vote_precinct_minnie[remove_Precinct])


# main function for controlling menu
def main():

    menu = ""

    while menu.lower() != "e":
        menu = input("""

[A] Add Votes from a precinct
[B] Display all votes from all precincts
[C] Display Vote stats
[D] Remove a precinct and all votes from that precinct
[E] Quit


    """)

        if menu == "a":
            add_votes_precinct()
        elif menu == "b":
            display_votes()
        elif menu == "c":
            display_vote_stats()
        elif menu == "d":
            remove_precinct()
        else:
            print("The selected option is unavailable")


main()
