from yearn.partners.snapshot import Partner, Wrapper, WildcardWrapper


partners = [
    Partner(
        name='coinomo',
        treasury='0xd3877d9df3cb52006b7d932e8db4b36e22e89242',
        wrappers=[
            Wrapper(
                name='yvUSDC',
                vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                wrapper='0xd3877d9df3cb52006b7d932e8db4b36e22e89242',
            ),
        ],
    ),
    Partner(
        name='alchemix',
        treasury='0x8392F6669292fA56123F71949B52d883aE57e225',
        wrappers=[
            Wrapper(
                name='dai',
                vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                wrapper='0x014dE182c147f8663589d77eAdB109Bf86958f13',
            ),
            Wrapper(
                name='dai-2',
                vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                wrapper='0x491EAFC47D019B44e13Ef7cC649bbA51E15C61d7',
            ),
        ],
    ),
    Partner(
        name='inverse',
        treasury='0x926dF14a23BE491164dCF93f4c468A50ef659D5B',
        wrappers=[
            Wrapper(
                name='dai-wbtc',
                vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                wrapper='0xB0B02c75Fc1D07d351C991EBf8B5F5b48F24F40B',
            ),
            Wrapper(
                name='dai-yfi',
                vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                wrapper='0xbE21650b126b08c8b0FbC8356a8B291010ee901a',
            ),
            Wrapper(
                name='dai-weth',
                vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                wrapper='0x57faa0dec960ed774674a45d61ecfe738eb32052',
            ),
            Wrapper(
                name='usdc-weth',
                vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                wrapper='0x698c1d40574cd90f1920f61D347acCE60D3910af',
            ),
            Wrapper(
                name='dola-stabilizer',
                vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                wrapper='0x973F509c695cffcF355787456923637FF8A34b29',
            ),
        ],
    ),
    Partner(
        name='frax',
        treasury='0x8d0C5D009b128315715388844196B85b41D9Ea30',
        wrappers=[
            Wrapper(
                name='usdc',
                vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                wrapper='0xEE5825d5185a1D512706f9068E69146A54B6e076',
            ),
        ],
    ),
    Partner(
        name='pickle',
        treasury='0x066419EaEf5DE53cc5da0d8702b990c5bc7D1AB3',
        wrappers=[
            Wrapper(
                name='usdc',
                vault='0x5f18C75AbDAe578b483E5F43f12a39cF75b973a9',
                wrapper='0xEecEE2637c7328300846622c802B2a29e65f3919',
            ),
            Wrapper(
                name='lusd',
                vault='0x5fA5B62c8AF877CB37031e0a3B2f34A78e3C56A6',
                wrapper='0x699cF8fE0C1A6948527cD4737454824c6E3828f1',
            ),
        ],
    ),
    Partner(
        name='badger',
        treasury='0xB65cef03b9B89f99517643226d76e286ee999e77',
        wrappers=[
            Wrapper(
                name='wbtc',
                vault='0xA696a63cc78DfFa1a63E9E50587C197387FF6C7E',
                wrapper='0x4b92d19c11435614CD49Af1b589001b7c08cD4D5',
            ),
        ],
    ),
    Partner(
        name='deus',
        treasury='0x4e8a7c429192bfda8c9a1ef0f3b749d0f66657aa',
        wrappers=[
            Wrapper(
                name='aeth',
                vault='0x132d8D2C76Db3812403431fAcB00F3453Fc42125',
                wrapper='0x4e8a7c429192bfda8c9a1ef0f3b749d0f66657aa',
            )
        ],
    ),
    Partner(
        name='basketdao',
        treasury='0x7301C46be73bB04847576b6Af107172bF5e8388e',
        wrappers=[
            Wrapper(
                name='crvLINK-v2',
                vault='0xf2db9a7c0ACd427A680D640F02d90f6186E71725',
                wrapper='0x0309c98B1bffA350bcb3F9fB9780970CA32a5060',
            ),
            Wrapper(
                name='yvBOOST',
                vault='0x9d409a0A012CFbA9B15F6D4B36Ac57A46966Ab9a',
                wrapper='0x0309c98B1bffA350bcb3F9fB9780970CA32a5060',
            ),
        ],
    ),
    Partner(
        name='gb',
        treasury='0x6965292e29514e527df092659FB4638dc39e7248',
        wrappers=[
            WildcardWrapper(
                name='gb1',
                wrapper='0x6965292e29514e527df092659FB4638dc39e7248',
            ),
        ],
    ),
    Partner(
        name='donutapp',
        treasury='0x9eaCFF404BAC19195CbD131a4BeA880Abd09B35e',
        wrappers=[
            Wrapper(
                name='yvDAI',
                vault='0x19D3364A399d251E894aC732651be8B0E4e85001',
                wrapper='0x9eaCFF404BAC19195CbD131a4BeA880Abd09B35e',
            ),
        ],
    ),
    Partner(
        name="yieldster",
        treasury='0x2955278aBCE187315D6d72B0d626f1217786DF60',
        wrappers=[
            Wrapper(
                name="liva-one",
                vault=None,
                wrapper="0x2747ce11793F7059567758cc35D34F63ceE8Ac00"
                ),
            ],
        ),
]
