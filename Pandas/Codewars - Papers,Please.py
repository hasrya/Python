

class Inspector:
    bulletins = ()
    pass


    def receive_bulletin(self, bulletin):
        '''
        Updates to the list of nations (comma-separated if more than one) whose citizens may enter (begins empty, before the first bulletin):
        example 1: Allow citizens of Obristan
        example 2: Deny citizens of Kolechia, Republia
        #Todo - change to global list of 1. Allowed Countries, 2. Denied Countries


        Updates to required documents
        example 1: Foreigners require access permit
        example 2: Citizens of Arstotzka require ID card
        example 3: Workers require work pass
        #Todo - change to global list of 1. Requirements
        #Todo - x3 objects -> Foreigners, Citizens, Workers

        Updates to required vaccinations
        example 1: Citizens of Antegria, Republia, Obristan require polio vaccination
        example 2: Entrants no longer require tetanus vaccination
        #Todo - change to global list of 1. Requirements

        Update to a currently wanted criminal
        example 1: Wanted by the State: Hubert Popovic
        #Todo - Update to global list of criminals
         - List of criminals must be reset after each bulletin. Only valid for the given day
        '''

        pass

    def inspect(self, obj):
        '''
        Each day, a number of entrants line up outside the checkpoint inspection booth to gain
        passage into Arstotzka.
        The inspect method will receive an object representing each entrant's set of
        identifying documents.
        This object will contain zero or more properties which represent separate documents.
        Each property will be a string value. These properties may include the following:

        Applies to all entrants:
        passport
        certificate_of_vaccination
        Applies only to citizens of Arstotzka
        ID_card
        Applies only to foreigners:
        access_permit
        work_pass
        grant_of_asylum
        diplomatic_authorization
        The inspect method will return a result based on whether the entrant passes or fails inspection:
        #Todo - Object properties:
        # All -> passport;
        # Citizen -> ID_card
        # Foreigner -> access_permit, work_pass, grant_of_asylum, diplomatic_authorization

        #Todo - To confirm if the passed object contains the given properties
            # Object.type = [Citizen, Foreigner]
            # Object.documents = [x,y,z]


        Conditions for passing inspection

        All required documents are present
        There is no conflicting information across the provided documents
        All documents are current (ie. none have expired) -- a document is
        considered expired if the expiration date is November 22, 1982 or earlier
        The entrant is not a wanted criminal
        If a certificate_of_vaccination is required and provided,
        it must list the required vaccination
        A "worker" is a foreigner entrant who has WORK listed as their purpose on
        their access permit
        If entrant is a foreigner, a grant_of_asylum or diplomatic_authorization are acceptable in
        lieu of an access_permit. In the case where a diplomatic_authorization is used, it must include
        Arstotzka as one of the list of nations that can be accessed.


        :return
            pass:
                If the entrant is a citizen of Arstotzka: Glory to Arstotzka.
                If the entrant is a foreigner: Cause no trouble.

            fail1: - expired or missing document, or certificate_of_vaccination does not include
            necessary vaccine:
                Example 1: Entry denied: passport expired.
                Example 2: Entry denied: missing required vaccination.
                Example 3: Entry denied: missing required access permit.

            fail2: -
                'detainment'

            *** denial and detainment *** -> Priority = Detain;

        '''

        pass



'''
TEST EXAMPLE:

bulletin = """Entrants require passport
Allow citizens of Arstotzka, Obristan"""

inspector = Inspector()
inspector.receive_bulletin(bulletin)

entrant1 = {
    "passport": """ID#: GC07D-FU8AR
    NATION: Arstotzka
    NAME: Guyovich, Russian
    DOB: 1933.11.28
    SEX: M
    ISS: East Grestin
    EXP: 1983.07.10"""
}

inspector.inspect(entrant1) #=> 'Glory to Arstotzka.'

'''