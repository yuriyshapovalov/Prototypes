using System;
using System.Collections;

namespace Collections
{
    class BitArray_p
    {
        private BitArray bitArray;
        private BitArray bitArray1;
        private BitArray bitArray2;

        public BitArray_p()
        {
            bitArray = new BitArray(5);
            Console.WriteLine("Default BitArray of 5 elements: {0}", PrintBitArray(bitArray));

            bitArray[1] = true;
            bitArray[3] = true;
            Console.WriteLine("Element 1 and 3 has been changed: {0}", PrintBitArray(bitArray));

            bitArray1 = new BitArray(new byte[] { 213, 72 });
            Console.WriteLine("New BitArray from byte array [213, 72]: {0}", PrintBitArray(bitArray1));

            bitArray2 = new BitArray(new bool[] { false, true, true, false, true });
            Console.WriteLine("New BitArray from boolean array [false, true, true, false, true]: {0}", PrintBitArray(bitArray2));

            Console.WriteLine("First and second BitArray count: {0}, {1}", bitArray.Count, bitArray1.Count);

            bitArray.And(bitArray2);
            Console.WriteLine("And operation on bit array 1 and 3: {0}", PrintBitArray(bitArray));

            bitArray.Or(bitArray2);
            Console.WriteLine("Or operation on bit array 1 and 3: {0}", PrintBitArray(bitArray));

            bitArray.Not();
            Console.WriteLine("Not operation on bit array 1: {0}", PrintBitArray(bitArray));

            bitArray.Xor(bitArray2);
            Console.WriteLine("Xor operation on bit array 1 and 3: {0}", PrintBitArray(bitArray));

            bitArray.Set(3, true);
            Console.WriteLine("Set element 3 to true: {0}", PrintBitArray(bitArray));

        }

        private string PrintBitArray(BitArray array, string arrayName = null)
        {
            string arrayString = string.Empty;

            if (arrayName != string.Empty)
                arrayString += arrayName + ": ";

            foreach (object obj in array)
            {
                arrayString += obj.ToString() + " ";
            }

            return arrayString;
        }
    }
}
