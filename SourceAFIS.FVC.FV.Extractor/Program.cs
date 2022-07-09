// Part of SourceAFIS extractor for FVC FV: https://sourceafis.machinezoo.com/fvc
using System;
using System.IO;

namespace SourceAFIS.FVC.FV.Extractor;

public class Program
{
    static int Main(string[] args)
    {
        if (args.Length != 3)
        {
            Console.WriteLine("Usage: enroll.exe <imagefile> <templatefile> <outputfile>");
            return 1;
        }
        byte[] template = null;
        try
        {
            template = new FingerprintTemplate(new FingerprintImage(File.ReadAllBytes(args[0]))).ToByteArray();
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex);
        }
        try
        {
            if (template != null)
                File.WriteAllBytes(args[1], template);
            File.AppendAllText(args[2], string.Format("{0} {1} {2}", args[0], args[1], template != null ? "OK" : "FAIL"));
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex);
            return 1;
        }
        return 0;
    }
}
