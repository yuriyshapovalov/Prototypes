using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;
using System.Net.NetworkInformation;

namespace Net
{
    public class Sniffer
    {
        public static void Main()
        {
            Console.WriteLine("Sniff");

            TcpListener listner = new TcpListener(80);

            listner.Start();

            Console.ReadKey();
        }
    }
}
