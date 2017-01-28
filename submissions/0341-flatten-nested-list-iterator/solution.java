public class NestedIterator implements Iterator<Integer> {
    private List<Integer> valueList = new ArrayList<>();
    private Integer[] valueArray;
    private int currentValueCursor = -1;
    private int size = 0;

    public NestedIterator(List<NestedInteger> nestedList) {
        for (NestedInteger nestedInteger : nestedList) {
            deepExtractNestedInteger(nestedInteger);
        }
        valueArray = valueList.toArray(new Integer[0]);
        valueList = null;
        size = valueArray.length;
    }

    @Override
    public Integer next() {
        if (!hasNext()) {
            return null;
        } else {
            currentValueCursor++;
            return valueArray[currentValueCursor];
        }
    }

    @Override
    public boolean hasNext() {
        return currentValueCursor + 1 < size;
    }

    private void deepExtractNestedInteger(NestedInteger extractingRaw) {
        if (extractingRaw.isInteger()) {
            valueList.add(extractingRaw.getInteger());
        } else {
            List<NestedInteger> list = extractingRaw.getList();
            for (NestedInteger nestedInteger : list) {
                deepExtractNestedInteger(nestedInteger);
            }
        }
    }
}
