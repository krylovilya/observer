from observer import Subject, Observer


def main():
    ellis = Observer("Ellis")
    george = Observer("George")
    thomas = Observer("Thomas")
    nicholas = Observer("Nicholas")
    scott = Observer("Scott")

    fedora = Subject("Fedora", ellis, george, thomas)
    opensuse = Subject("OpenSuse", nicholas, scott)

    test_string = "{observer_name} found out that a new version {status} " \
                  "of his favorite Linux distribution {subject_name} was released."

    opensuse.set("14.0")
    opensuse.notify(test_string)

    fedora.set("29")
    fedora.notify(test_string)

    opensuse.set("15.0")
    opensuse.notify(test_string)


if __name__ == "__main__":
    main()
