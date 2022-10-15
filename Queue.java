public class Queue<E>
{
//Stacks initially empty - they are 'new'
    private Stack<E> in_stack = new Stack<E>();
    private Stack<E> out_stack = new Stack<E>();

    public E dequeue() { //FIFO queue implemented using 2 stacks
        if (out_stack.isEmpty()) {
            while (in_stack.isEmpty() == False) {
               out_stack.push(in_stack.pop());
            }
        }
        return out_stack.pop();
    }

    public void queue(E elem) {
        in_stack.push(elem);
    }

}
