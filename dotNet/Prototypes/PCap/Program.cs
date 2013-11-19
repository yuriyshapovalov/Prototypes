using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PCap
{
    class Program
    {
        static void Main(string[] args)
        {
            var devices = SharpPcap.CaptureDeviceList.Instance;

            foreach (var dev in devices)
            {
                Console.WriteLine("{0} - {1}", dev.Name, dev.Description);
            }

            var device = devices[1];

            device.OnPacketArrival += Program_OnPacketArrival;
            device.Open(SharpPcap.DeviceMode.Promiscuous);

            device.StartCapture();

            Console.ReadKey();
            device.StopCapture();
        }

        static void Program_OnPacketArrival(object sender, SharpPcap.CaptureEventArgs e)
        {
            var packet = PacketDotNet.Packet.ParsePacket(PacketDotNet.LinkLayers.Ethernet, e.Packet.Data);
        }
    }
}
