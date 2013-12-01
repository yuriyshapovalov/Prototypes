using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Collections
{
    // http://msdn.microsoft.com/ru-ru/library/system.collections.stack%28v=vs.110%29.aspx
    class Stack_p
    {
        public Stack_p()
        {
            Stack stack = new Stack();
            stack.Push("hello");
            stack.Push("world");
            stack.Push("foo");

            Console.WriteLine("Elements in stack after pushing some: {0}", stack.Count);

            Console.WriteLine("Peek top element but not remove in: {0}", stack.Peek());

            Console.WriteLine("Popped element from stack: {0}", stack.Pop());

            Console.WriteLine("Elements in stack: {0}", stack.Count);

            Console.WriteLine("Is stack synchronized: {0}", stack.IsSynchronized);
        }
    }
}
