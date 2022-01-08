def createSite(results):
    with open("result.html", "w") as r:

        r.write("<body>\n\t<table border='1'>")
        for result in results:
            r.write("<tr><td><table>")
            results[result]["result"]
            r.write(f"\n\t\t<tr><th>Słowo: {result}</th></tr>")
            r.write(f"\n\t\t<tr><th>Czas: {results[result]['time']}</th></tr>")
            for word in results[result]["result"][::-1]:
                r.write(f"\n\t\t<tr><td><center>{word}</center></td></tr>")
            r.write("</table></td></tr>")
        r.write("\n\t</table></table>\n</body>")
