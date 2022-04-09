import java.util.ArrayList;
import java.util.Optional;

public class Pile<T> {
    ArrayList<T> data_ = new ArrayList<>();

    Optional<T> peek() {
        if (empty())
            return Optional.empty();

        return Optional.of(data_.get(data_.size() - 1));
    }

    Optional<T> pop() {
        if (empty())
            return Optional.empty();

        var ret = peek();
        data_.remove(data_.size() - 1);
        return ret;
    }

    void push(T elem) {
        data_.add(elem);
    }

    boolean empty() {
        return data_.isEmpty();
    }
}
