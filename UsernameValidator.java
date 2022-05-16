import java.util.Scanner;
class UsernameValidator {
    /*
     * Write regular expression here.
     */
    public static final String regularExpression = "([a-zA-Z])(\\w){7,29}";

    /*
    From HackerRank:
    ^ represents that starting character of the string. [a-zA-Z] makes sure that the starting character is in
    the lowercase or uppercase alphabet. \\w represents a check to make sure that the remaining items are word
    items, which includes the underscore. The {7,29} represents the 8-30 character constraint given to us minus the
    predefined first character.
    */
}