using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int maxInt = int.Parse(Console.ReadLine());
        int radius = maxInt / 2;
        List<string> array = new List<string>();

        for (int i = 0; i < maxInt; i++)
        {
            string line = Console.ReadLine();
            array.Add(line);
        }

        int result = 0;
        for (int i = 0; i < radius; i++) {
            if (array[i] == array[i + radius])
            {
                result += 2;
            }
        }
        Console.WriteLine(result);
    }
}