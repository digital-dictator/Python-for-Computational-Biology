from Bio.Blast import NCBIXML
for record in NCBIXML.parse(open("NC_003197.xml")):
    #We want to ignore any queries with no search results:
    if record.alignment:
        print("QUERY: %s..." % record.query[:60])
        for align in record.alignments:
            for hsp in align.hsps:
                print(" %s HSP, e=%f, from position %i to %i" \
                % (align.hit_id, hsp.expect, hsp.query_start, hsp.query_end))
print ("Done")
for record in NCBIXML.parse(output_handle):
    #We want to ignore any queries with no search results:
    if record.alignments:
        print("QUERY: %s..." % record.query[:60])
        for align in record.alignments:
            for hsp in align.hsps:
                print(" %s HSP, e=%f, from position %i to %i" \
                % (align.hit_id, hsp.expect, hsp.query_start, hsp.query_end)
                assert hsp.expect <= E_VALUE_THRESH)
print("Done")
